<template>
  <div class="extension">
    <div class="row mb-4">
      <div class="col-2">
        <label for="url">URL</label>
      </div>
      <div class="col-10">
        <input v-model="url" type="text" id="url" name="url">
      </div>
    </div>
    <div class="d-flex fl-end">
      <button type="button" class="ps-btn btn-primary ps-btn" @click="getUrl">Get URL</button>
      <button :disable="!url" type="button" class="ps-btn btn-primary" @click="scanUrl">Scan URL</button>
    </div>
  </div>
</template>
<script>
import axios from 'axios'

const URL = 'http://18.166.71.250/get_phishing_url'
const LABEL = {
  good: 'good',
  bad: 'bad'
}

export default {
  data() {
    return {
      loading: false,
      url: ''
    }
  },

  computed: {

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
      const { data } = await axios.post(URL, {
        url: this.url
      })
      if (data.label === LABEL.good) {
        alert('Its ok')
      } else {
        alert('So bad')
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
</style>