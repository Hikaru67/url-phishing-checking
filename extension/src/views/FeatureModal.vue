<template>
  <div v-if="isOpen">
    <!-- <Modal
      centered
      title="Action Detail"
      v-model="isOpen"
      id="modal-lg"
      size="lg"
      hide-footer
      @hide="cancel"
    > -->
      <div class="mt-1">

      </div>
      <div class="d-flex justify-content-between my-2">
        <button variant="danger" @click="cancel">Cancel</button>
      </div>
    <!-- </Modal> -->
  </div>
</template>

<script>
export default {
  data() {
    return {
      isOpen: false,
      isUpdate: false,
    };
  },
  methods: {
    async openUpdateModal(action){
      this.model = action;
      this.isOpen = true;
      this.isUpdate = true;
    },

    cancel(){
      this.isOpen = false;
      this.isUpdate = false;
      this.model = {};
      this.$emit('loadData')
    },

    getTitle(url) {
      return url ? url.slice(8) : ''
    },

    getBody(data) {
      if (typeof data === 'object') {
        const keys = Object.keys(data)
        if (keys.length === 1 && keys[0] === 'data') {
          data = JSON.stringify(JSON.parse(data.data))
          return data
        }
      }
      return JSON.stringify(data)
    }
  },
};
</script>
<style lang="scss" scoped>
  label {
    font-size: 16px;
    margin-top: 0.3rem;
    margin-bottom: 0;
  }
</style>
