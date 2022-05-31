<template>
  <div>
    <img class="background" src="../../public/background.png" alt="" />
    <div class="extension">
      <div class="row mb-2 mt-2">
        <div class="text-center">
          {{ getDomain }}
          <!-- <input v-model="url" type="text" id="url" name="url"> -->
        </div>
      </div>
      <div class="m-auto">
        <div class="circle small" :data-fill="percent" hour :style="getColor">
          <span>{{ percent }}%</span>
          <div class="bar"></div>
        </div>
      </div>
      <div class="text-center mb-2" :class="label ? 'status' : 'status-alert'">{{ getStatus }}</div>
      <button v-if="features.length" type="button" class="btn btn-success mb-2">Xem chi tiết</button>
      <button type="button" class="btn btn-report">Báo cáo</button>
    </div>
  </div>
</template>
<script>
import axios from 'axios'

const URL_MC = process.env.VUE_APP_URL

const LABEL = {
  good: 'good',
  bad: 'bad'
}

export default {
  data() {
    return {
      loading: false,
      url: 'https://github.com/karl-lunarg',
      label: 1,
      features: [],
      percent: 80,
    }
  },

  computed: {
    getDomain() {
      const url =  new URL(this.url)
      return url.origin
    },
    
    getColor() {
      if (this.percent > 60) { return '--color:#28a745' }
      if (this.percent > 40) { return '--color:#d9f117' }
      return '--color:#dc3545'
    },

    getStatus() {
      return this.label ? 'Website này có thể an toàn.' : 'Website này không an toàn.'
    }
  },

  created() {
    this.getUrl()
  },

  mounted() {
    this.scanUrl()
  },

  methods: {
    async getUrl() {
      this.loading = true;
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
        }, (result) => {
          this.url = result[0].result
        });
        this.loading = false;
      } catch (e) {
        this.loading = false;
      }
    },

    async scanUrl() {
      const { data } = await axios.post(URL_MC, {
        url: this.url
      })
      if (data.label === LABEL.good) {
        this.label = 1
        this.percent = data.percent
        this.features = data.percent
      } else {
        this.label = 1
        this.percent = data.percent
        this.features = data.percent
      }
    }
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
  color: green;
}
.status-alert {
  color: red;
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
</style>