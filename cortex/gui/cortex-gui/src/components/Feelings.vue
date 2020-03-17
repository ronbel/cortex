<template>
  <h2 v-if="error">No data found</h2>
  <div v-else class="feelings-container">
    <div v-if="!feelingsReady" class="loading-overlay">
      <Loading />
    </div>

    <ProgressBar
      :font-size="20"
      text-fg-color="red"
      bar-color="red"
      class="progress-bar"
      text="Hunger"
      size="50"
      :val="feelingsDetails.hunger * 100"
      max="100"
    />
    <ProgressBar
      :font-size="20"
      text-fg-color="blue"
      bar-color="blue"
      class="progress-bar"
      text="Thirst"
      size="50"
      :val="feelingsDetails.thirst * 100"
      max="100"
    />
    <ProgressBar
      :font-size="20"
      text-fg-color="green"
      bar-color="green"
      class="progress-bar"
      text="Exhaustion"
      size="50"
      :val="feelingsDetails.exhaustion * 100"
      max="100"
    />
    <ProgressBar
      :font-size="20"
      text-fg-color="yellow"
      bar-color="yellow"
      class="progress-bar"
      text="Happiness"
      size="50"
      :val="feelingsDetails.happiness * 100"
      max="100"
    />
  </div>
</template>

<script>
import ProgressBar from "vue-simple-progress";
import Loading from "./Loading";
import { getSnapshotResult } from "../services/api.service";

export default {
  data() {
    return {
      feelingsReady: false,
      feelingsDetails: { hunger: 0, thirst: 0, happiness: 0, exhaustion: 0 },
      error: false
    };
  },
  components: {
    ProgressBar,
    Loading
  },
  created() {
    getSnapshotResult(
      this.$props.userId,
      this.$props.snapshotId,
      "feelings"
    ).then(data => {
      setTimeout(() => {
        this.feelingsDetails = data;
        this.feelingsReady = true;
      }, 1000);
    }).catch(() => this.error = true);
  },
  props: ["userId", "snapshotId"]
};
</script>


<style lang="scss" scoped>
.feelings-container {
  display: flex;
  flex-direction: column;
  flex: 1;
  width: 100%;
  justify-content: center;
  align-items: "center";
}

.progress-bar {
  margin-bottom: 10px;
  min-width: 350px;
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