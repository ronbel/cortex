<template>
  <div class="snapshots-section">
    <div @click="$emit('close')" class="close" />
    <h1>Snapshots</h1>
    <h2>{{`Of Specimen #${userId}`}}</h2>

    <Loading v-if="!snapshotsReady" />
    <transition-group
      @after-appear="removeDelay"
      @before-appear="addDelay"
      appear
      name="flying"
      v-else-if="selectedSnapshot === null"
      class="snapshots-grid"
    >
      <SnapshotCard
        v-for="(snapshot, index) in snapshotsList"
        :data-index="index"
        :key="snapshot._id"
        :snapshot="snapshot"
        @click="setSnapshot"
      />
    </transition-group>

    <SnapshotDetails :snapshotId="selectedSnapshot" :userId="userId" @back="setSnapshot(null)" v-else />
  </div>
</template>

<script>
import SnapshotCard from "./SnapshotCard";
import SnapshotDetails from "./SnapshotDetails";
import Loading from "./Loading";
import { getUserSnapshots } from "../services/api.service";

export default {
  data() {
    return { selectedSnapshot: null, snapshotsList: [], snapshotsReady: false };
  },
  props: ["userId"],
  components: {
    SnapshotCard,
    SnapshotDetails,
    Loading
  },
  methods: {
    setSnapshot(id) {
      this.selectedSnapshot = this.selectedSnapshot === id ? null : id;
    },
    addDelay(el) {
      el.style.transitionDelay = `${100 * el.dataset.index}ms`;
    },
    removeDelay(el) {
      el.style["transition-delay"] = "0ms";
    }
  },
  created() {
    getUserSnapshots(this.$props.userId).then(data => {
      setTimeout(() => {
        this.snapshotsList = data;
        this.snapshotsReady = true;
      }, 1500);
    });
  }
};
</script>

<style lang="scss" scoped>
.snapshots-section {
  height: 90vh;
  width: 50vw;
  background: var(--secondary-color);
  border-radius: 10%;
  display: flex;
  flex-direction: column;
  position: relative;
  padding-bottom: 35px;
  padding-right: 15px;
  padding-left: 15px;

  h1,
  h2 {
    color: var(--main-color);
  }

  h1 {
    margin-bottom: 0;
  }

  .close {
    position: absolute;
    top: 30px;
    left: 45px;
    background-image: url("../assets/close.png");
    width: 32px;
    height: 32px;
    cursor: pointer;
    background-size: contain;
  }
}

.snapshots-grid {
  display: grid;
  flex: 1;
  grid-template-columns: repeat(2, 1fr);
  grid-column-gap: 10px;
  grid-row-gap: 40px;
  padding-left: 25px;
  padding-right: 25px;
  overflow-y: scroll;
  overflow-x: hidden;

  &::-webkit-scrollbar-track {
    -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.1);
    background-color: #f5f5f5;
    border-radius: 10px;
  }

  &::-webkit-scrollbar {
    width: 10px;
    background-color: #f5f5f5;
    border-radius: 10px;
  }

  &::-webkit-scrollbar-thumb {
    border-radius: 10px;
    background-color: var(--main-color);
  }
}

.flying-enter-active,
.flying-leave-active {
  transition: transform 200ms ease, opacity 200ms ease;
}
.flying-enter,
.flying-leave-to {
  transform: translateX(200px);
  opacity: 0;
}
.flying-enter-to,
.flying-leave {
  transform: translateX(0);
  opacity: 1;
}
</style>