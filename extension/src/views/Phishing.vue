<template>
  <div class="extension">
    <div class="row mb-4">
      <div class="col-3">
        <label for="url">URL</label>
      </div>
      <div class="col-9">
        <input v-model="url" type="text" id="url" name="url">
      </div>
    </div>
    <div class="d-flex fl-end">
      <button type="button" class="ps-btn btn-primary ps-btn" @click="getUrl">Get URL</button>
      <button type="button" class="ps-btn btn-primary" @click="scanUrl">Scan URL</button>
    </div>
  </div>
</template>
<script>
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
        console.log('🚀 ~ res', res)
        this.loading = false;
      } catch (e) {
        this.loading = false;
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