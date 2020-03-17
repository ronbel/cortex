<template>
  <h2 v-if="error"></h2>
  <div v-else class="depth-container">
    <div v-if="!imageReady" class="loading-overlay">
      <Loading />
    </div>
    <div class="size">Size: {{`${imageInfo.width}x${imageInfo.height}`}}</div>
    <img :src="imageUrl" class="image" v-show="showImage" />
    <div
      @click="showImage = !showImage"
      class="show-button"
    >{{`${showImage ? 'Hide' : 'Show'} Image`}}</div>
  </div>
</template>


<script>
import Loading from "./Loading";
import {
  getSnapshotResult,
  getSnapshotResultDataUrl
} from "../services/api.service";

export default {
  data() {
    return {
      showImage: false,
      error: false,
      imageReady: false,
      imageInfo: { width: "", height: "" },
    };
  },
  components: { Loading },
  props: ["userId", "snapshotId", "type"],
  created() {
    getSnapshotResult(
      this.$props.userId,
      this.$props.snapshotId,
      this.$props.type
    )
      .then(data => {
        setTimeout(() => {
          this.imageInfo = data;
          this.imageReady = true;
        }, 1000);
      })
      .catch(() => (this.error = true));
  },
  computed: {
    imageUrl() {
      return getSnapshotResultDataUrl(this.$props.userId, this.$props.snapshotId, this.$props.type);
    }
  }
};
</script>

<style lang="scss" scoped>
.size {
  color: var(--main-color);
  font-size: 25px;
  width: 100%;
  height: 40px;
}

.depth-container {
  display: flex;
  flex: 1;
  flex-direction: column;
  align-items: center;
}

.show-button {
  width: 150px;
  height: 50px;
  color: white;
  border: 2px white solid;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.2rem;
  cursor: pointer;
  transition: border-color 200ms ease-in-out, color 200ms ease-in-out;

  &:hover {
    border-color: var(--main-color);
    color: var(--main-color);
  }
}

.image {
  width: 300px;
  height: 300px;
  margin-top: 10px;
  margin-bottom: 10px;
}

.loading-overlay {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #00000055;
}
</style>