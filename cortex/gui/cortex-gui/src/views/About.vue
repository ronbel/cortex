<template>
    <div class="container">
        <h1 class="title">About</h1>
        <p class="text">
            Cortex is a project created for the Advanced System Design class in Tel Aviv University. <br/>
            This GUI was made using Vue.js and Flask. The rest of the project also uses Flask, as well as pymongo <br/>
            and MongoDB, Protobuf, RabbitMQ and Docker. <br/> <br/>
            Created by Ron Belkin <br/>
            The logo and theme colors were taken from <a href="http://obrainlab.com/">here</a>, <strong>for non-commerical use</strong> (Please don't sue me 😅)
        </p>
        <router-link class="button" exact to="/">Back</router-link>
    </div>
</template>

<script>
export default {
    
}
</script>


<style lang="scss" scoped>
    .container{
        display: flex;
        flex-direction: column;
        align-items: center;
        flex: 1;
    }

   .title{
        font-size: 3em;
        color: var(--secondary-color);
        font-weight: bold;
    }

    .text{
        font-size: 1.5rem;
        line-height: 1.8rem;
    }
</style>