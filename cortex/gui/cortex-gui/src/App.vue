<template>
  <div id="app">
    <transition name="screen">
      <router-view></router-view>
    </transition>
  </div>
</template>

<script>



export default {
  name: 'App'
  
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Roboto+Condensed');

:root{
--main-color: #FFC107;
--secondary-color: #3B3B3B;
}

* {
        box-sizing: border-box;
        font-family: "Roboto Condensed", sans-serif;
    }

 html, body {
        margin: 0;
        width: 100%;
        height: 100%;
    }

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: #CCC;
  width: 100%;
  height: 100%;
  display: flex;
}

 .screen-leave-active, .screen-enter-active {
        transition: transform 0.5s ease, opacity 0.5s ease;
    }
    .screen-enter-active {
        transition-delay: 500ms;
    }
    .screen-enter, .screen-leave-to {
        opacity: 0;
        transform: translateX(-100%);
    }
    .screen-enter-to, .screen-leave {
        opacity: 1;
        transform: translateX(0);
    }

  .button{
        display: flex;
        justify-content: center;
        align-items: center;
        width: 110px;
        height: 50px;
        text-decoration-line: none;
        color: var(--main-color);
        background-color: var(--secondary-color);
        font-size: 2rem;
        border-radius: 15px;
        transition: filter 200ms ease-in-out;

        &:hover{
            filter: brightness(1.7);
        }
    }

</style>
