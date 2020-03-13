<template>
    <div class="container">
        <img class="logo" alt="Cortex logo" src="../assets/cortex-logo.png">

        <h1 class="title">Welcome to Cortex!</h1>

        <div class="buttons-container">
            <router-link class="button" exact to="/users">Users</router-link>
            <router-link class="button" exact to="/about">About</router-link>
        </div>
    </div>
</template>


<script>
export default {
    
}
</script>

<style lang="scss" scoped>
    .container{
        display: flex;
        flex: 1;
        flex-direction: column;
        align-items: center;
        padding-top: 20px;
    }

    .logo{
        width: 350px;
        height: 350px;
    }

    .title{
        font-size: 3em;
        color: var(--secondary-color);
        font-weight: bold;
    }

    .buttons-container{
        display: flex;
        width: 40%;
        justify-content: space-between;
        align-items: center;
    }


</style>