<template>
  <div>
    <img class="background" src="../../public/background.png" alt="" />
    <div class="extension">
      <div v-if="loading" class="loader" />
      <div :class="loading ? 'shader' : ''">
        <div class="row mb-2 mt-2">
        <div class="text-center">
          {{ getDomain }}
        </div>
        </div>
        <div class="m-auto">
          <div class="circle small" :data-fill="percent" hour :style="getColor">
            <span>{{ percent }}%</span>
            <div class="bar"></div>
          </div>
        </div>
        <div class="text-center mb-2" :class="!label ? 'status' : 'status-alert'">{{ getStatus }}</div>
      </div>
      <button :disabled="!features.length" type="button" class="btn btn-success mb-2" @click="showFeatures">Xem chi tiết</button>
      <ul v-if="isFeaturesVisible" class="d-flex features-list">
        <li v-for="feature in getFeatureKey" :key="feature" class="feature" :class="getFeatureColor(feature, features[FEATURES[feature]])">{{ feature }}</li>
      </ul>
      <button type="button" class="btn btn-report" @click="prepareReport">Báo cáo</button>
      <div v-if="isReportVisible" class="mt-3 report d-flex content-center">
        <font-awesome-icon class="ml-2 thumb" :class="(report === 1) ? 'like' : ''" icon="fa-solid fa-thumbs-up" @click="like" />
        <font-awesome-icon class="ml-2 thumb" :class="(report === 2) ? 'dislike' : ''" icon="fa-solid fa-thumbs-down" @click="dislike" />
      </div>
      <div class="thanks">
        <p>Cảm ơn bạn đã báo cáo kết quả!</p>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import { FEATURES } from './../config'

const URL_MC = process.env.VUE_APP_URL

const LABEL = {
  good: 'good',
  bad: 'bad'
}

const PHISHING = 1
const LEGATE = 0

export default {
  components: {
  },
  data() {
    return {
      loading: false,
      url: '',
      label: 1,
      features: [],
      percent: 0,
      blockList: [],
      isFiltered: false,
      isFeaturesVisible: false,
      FEATURES,
      report: 0,
      isReportVisible: false
    }
  },

  computed: {
    getDomain() {
      if (!this.url) { return '...' }
      const url =  new URL(this.url)
      return url.origin
    },
    
    getColor() {
      if (this.percent > 60) { return '--color:#28a745' }
      if (this.percent > 40) { return '--color:#d9f117' }
      return '--color:#dc3545'
    },

    getStatus() {
      if (!this.url) { return '...' }
      const status = (!this.label ? 'Website này có thể an toàn.' : 'Website này không an toàn.') + (this.isFiltered ? '(Kết quả bộ lọc)' : '(Kết quả học máy)')
      return status
    },

    getFeatureKey() {
      return Object.keys(this.FEATURES)
    }
  },

  watch: {
    async url(val) {
      await this.scanUrl(this.url)
    }
  },

  async created() {
    await this.getBlockList()
    await this.getUrl()
  },

  methods: {
    async getUrl() {
      const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
      const tabId = tab.id;
      try {
        var res = await chrome.scripting.executeScript({
          target: { tabId: tabId },
          args: [],
          func: () => {
            const url = window.location.href
            return url ? url : ''
          }
        }, async (result) => {
          this.url = result[0].result
          if (this.url) {
            await this.scanUrl(this.url)
          }
        });
      } catch (e) {
        console.warn('getUrl => e', e)
      }
    },

    async scanUrl(url) {
      if (!url) {
        return
      }
      this.loading = true
      this.percent = 0
      const { data } = await axios.post(URL_MC, {
        url
      })
      this.clearData()
      this.isFiltered = !!data.is_filtered
      this.label = data.label
      if (data.label) {
        await this.setBlockList(url, data)
      }
      this.percent = Math.round(data.percent)
      this.features = data.features
      this.loading = false
    },

    async getBlockList() {
      const local = await chrome.storage.local.get("blocked")
      this.blockList = local.blocked
    },

    async setBlockList(url, data) {
      if (!data.label || !url) { return } // legate
      if (this.blockList.length && this.blockList.find(bl => bl.url === url)) { return }

      this.blockList.push({
        url,
        isFiltered: data.is_filtered
      })
      await chrome.storage.local.set({ blocked: this.blockList })
      this.getBlockList()
    },

    showFeatures() {
      // this.getUrl()
      console.log('this.blockList :>> ', this.blockList)
      this.isReportVisible = false
      this.report = 0
      this.isFeaturesVisible = !this.isFeaturesVisible
    },

    clearData() {
      this.label = null
      this.features = []
      this.percent = 0
      this.isFiltered = null
    },

    closeModal() {
      this.isFeaturesVisible = false
    },

    getFeatureColor(feature, value) {
      if (feature === 'Domain_Length') {
        if (value > 50) { return 'b-red' }
        if (value > 35) { return 'b-yellow' }
        return 'b-green'
      }
      if (feature === 'Subdomain_Level') {
        if (value > 6) { return 'b-red' }
        if (value > 3) { return 'b-yellow' }
        return 'b-green'
      }
      return value ? 'b-red' : 'b-green'
    },

    prepareReport() {
      this.isFeaturesVisible = false
      this.report = 0
      this.isReportVisible = !this.isReportVisible
    },

    like() {
      this.report = 1
    },

    dislike() {
      this.report = 2
    },
  }
}
</script>
<style lang="scss" scoped>
.ps-btn {
  border: none;
  min-height: 30px;
  border-radius: 5px;
  margin-right: 10px;
}
.fl-end {
  justify-content: flex-end;
}
.background {
  width: 320px;
  height: 100px;
}
.m-auto {
  width: 100px;
}
.status {
  font-size: 16px;
  color: #33a133;
}
.status-alert {
  color: red;
}
.b-green {
  background-color: green !important;
}
.b-red {
  background-color: #cd4747 !important;
}
.b-yellow {
  background-color: rgb(202, 202, 76) !important;
}
.btn {
  display: block;
  border-radius: 20px;
  margin: auto;
  color: white;
  min-width: 110px;
  height: 35px;
}
.btn-success {
  background-color: #28a745;
  border-color: #28a745;
}
.btn-report {
  background-color: rgb(65 66 94 / 98%);
  border-color: rgb(65 66 94 / 98%);
}
.thumb {
  &:hover {
    cursor: pointer;
  }
  font-size: 35px;
  display: inline-block;
  margin-left: 10px;
  color: #b3b3b3;
  &[data-icon='thumbs-up'] {
    &:hover {
      color: #33a133;
    }
  }
  &[data-icon='thumbs-down'] {
    &:hover {
      color: #cd4747;
    }
  }
}
.like {
  color: #33a133;
}
.dislike {
  color: #cd4747;
}
.shader {
  opacity: 0.3;
}

.features-list {
  flex-wrap: wrap;
  padding: 0;
  .feature {
    font-size: 12px;
    margin: 0.15rem;
    display: inline-block;
    color: #fff;
    padding: 0.2rem 0.5rem;
    border-radius: 25px;
  }
}

.report {
  justify-content: space-evenly
}
</style>