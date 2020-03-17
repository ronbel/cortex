<template>
  <div class="container">
    <div @click="$emit('back')" class="back" />
    <h2>Snapshot {{snapshotId}}</h2>
    <Loading v-if="!snapshotReady" />
    <div v-else class="buttons-section">
      <div
        @click="selectedResult = 'pose'"
        :class="['button','result-option', {selected: selectedResult === 'pose'}]"
      >Pose</div>
      <div
        @click="selectedResult = 'feelings'"
        :class="['button','result-option', {selected: selectedResult === 'feelings'}]"
      >Feelings</div>
      <div
        @click="selectedResult = 'depth_image'"
        :class="['button','result-option', {selected: selectedResult === 'depth_image'}]"
      >Depth</div>
      <div
        @click="selectedResult = 'color_image'"
        :class="['button','result-option', {selected: selectedResult === 'color_image'}]"
      >Color</div>
    </div>
    <Feelings :userId="userId" :snapshotId="snapshotId" v-if="selectedResult === 'feelings'" />
    <ImageView :key="selectedResult" type="depth_image" :userId="userId" :snapshotId="snapshotId" v-if="selectedResult === 'depth_image'" />
    <ImageView :key="selectedResult" type="color_image" :userId="userId" :snapshotId="snapshotId" v-if="selectedResult === 'color_image'" />
    <Pose :userId="userId" :snapshotId="snapshotId" v-if="selectedResult === 'pose'" />
  </div>
</template>

<script>
import Feelings from "./Feelings";
import ImageView from "./ImageView";
import Pose from "./Pose";
import Loading from "./Loading";
import { getSnapshot } from "../services/api.service";

export default {
  components: {
    Feelings,
    ImageView,
    Pose,
    Loading
  },
  data() {
    return {
      selectedResult: "",
      snapshotDetails: null,
      snapshotReady: false
    };
  },
  props: ["snapshotId", "userId"],
  created() {
    getSnapshot(this.$props.userId, this.$props.snapshotId).then(data => {
      setTimeout(() => {
        this.snapshotDetails = data;
        this.snapshotReady = true;
      }, 1000);
    });
  }
};
</script>


<style lang="scss" scoped>
.container {
  display: flex;
  flex: 1;
  flex-direction: column;
  align-items: center;
  padding-top: 15px;
  border-top: 3px gray solid;
  position: relative;
}

h2 {
  color: #c3c3c3;
}

.buttons-section {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 85%;
  margin-bottom: 20px;
}

.result-option {
  border: 1.5px silver solid;
  width: 135px;
  cursor: pointer;
  transition: border 200ms ease-in-out;

  &.selected {
    border-color: var(--main-color);
    border-width: 6px;
  }
}

.back {
  position: absolute;
  top: 5px;
  left: 10px;
  background-image: url("../assets/back.svg");
  background-size: cover;
  width: 55px;
  height: 55px;
  cursor: pointer;
}
</style>