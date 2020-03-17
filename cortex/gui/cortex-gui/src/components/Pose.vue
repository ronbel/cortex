<template>
  <h2 v-if="error">No data found</h2>
  <div v-else class="pose-container">
    <div v-if="!poseReady" class="loading-overlay">
      <Loading />
    </div>

    <div class="column">
      <h2>Translation</h2>
      <span>X: {{poseReady ? poseDetails.translation.x : ''}}</span>
      <span>Y: {{poseReady ? poseDetails.translation.y : ''}}</span>
      <span>Z: {{poseReady ? poseDetails.translation.z : ''}}</span>
    </div>

    <div class="column">
      <h2>Rotation</h2>
      <span>X: {{poseReady ? poseDetails.rotation.x : ''}}</span>
      <span>Y: {{poseReady ? poseDetails.rotation.y : ''}}</span>
      <span>Z: {{poseReady ? poseDetails.rotation.z : ''}}</span>
      <span>W: {{poseReady ? poseDetails.rotation.w : ''}}</span>
    </div>
  </div>
</template>


<script>
import { getSnapshotResult } from "../services/api.service";
import Loading from "./Loading";

export default {
  data() {
    return { poseReady: false, poseDetails: null, error: false };
  },
  props: ["userId", "snapshotId"],
  created() {
    getSnapshotResult(this.$props.userId, this.$props.snapshotId, "pose").then(
      data => {
        setTimeout(() => {
          this.poseDetails = data;
          this.poseReady = true;
        }, 1000);
      }
    ).catch(() => this.error = true);
  },
  components: { Loading }
};
</script>

<style lang="scss" scoped>
.pose-container {
  display: flex;
  justify-content: space-between;
  padding: 20px;
  flex: 1;
  position: relative;
  width: 80%;
}

.column {
  display: flex;
  flex-direction: column;

  h2 {
    color: var(--main-color);
    font-size: 1.8rem;
  }

  span {
    color: white;
    font-size: 1.4rem;
    margin-bottom: 10px;
  }
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