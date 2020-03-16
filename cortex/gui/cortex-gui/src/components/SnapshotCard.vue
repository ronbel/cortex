<template>
  <div @click="$emit('click', 'asfgavc')" class="card">
      <p>Serial Number faf5-89a31-bbb4-15hf492197</p>
      <h2>3/3/2020</h2>
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
  }
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