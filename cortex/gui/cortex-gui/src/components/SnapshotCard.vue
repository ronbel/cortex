<template>
  <div @click="$emit('click', snapshot._id)" class="card">
      <p>Serial Number {{snapshot._id}}</p>
      <h2>{{new Date(snapshot.datetime).toLocaleString('en-GB')}}</h2>
      <img class="logo" src="../assets/cortex-logo.png"/>
      <p class="more-details">More Details</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      expanded: false
    };
  },
  props: ['snapshot']
};
</script>

<style lang="scss" scoped>
.card {
  width: 100%;
  height: 120px;
  background-color: #2f4353;
  background-image: linear-gradient(205deg, #2f4353 0%, #d2ccc4 74%);
  position: relative;
  transition: filter 300ms ease-in-out;
  cursor: pointer;

    h2{
        margin-bottom: 10px;
    }

  .more-details{
      opacity: 0;
      transition: opacity 300ms ease-in-out;
      margin: 0;
  }

  &:hover{
      filter: brightness(1.3);

      .more-details{
          opacity: 1;
      }
  }
}


.logo{
    position: absolute;
    bottom: 10px;
    left: 15px;
    width: 30px;
    height: 30px;
}

</style>