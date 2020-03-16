<template>
  <div class="snapshots-section">
    <div @click="$emit('close')" class="close" />
    <h1>Snapshots</h1>
    <h2>Of Specimen #42</h2>

    <div v-if="selectedSnapshot === null" class="snapshots-grid">
      <SnapshotCard @click="setSnapshot" />
    </div>

    <SnapshotDetails @back="setSnapshot(null)" v-else/>
  </div>
</template>

<script>
import SnapshotCard from "./SnapshotCard";
import SnapshotDetails from "./SnapshotDetails"

export default {
    data(){
        return {selectedSnapshot: null}
    },
  components: {
    SnapshotCard,
    SnapshotDetails
  },
  methods: {
      setSnapshot(id){
          this.selectedSnapshot = this.selectedSnapshot === id ? null: id;
      }
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
    top: 20px;
    left: 35px;
    background-image: url("../assets/close.png");
    width: 32px;
    height: 32px;
    cursor: pointer;
    background-size:contain;
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
</style>