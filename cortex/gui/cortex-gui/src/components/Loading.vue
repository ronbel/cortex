<template>
    <div :style="containerStyle" class="box">
        <h2 :style="{color: 'white'}">Loading...</h2>
        <img class="pic" src="../assets/cortex-logo.png"/>
    </div>
</template>

<script>
export default {
    props: ['containerStyle']
}
</script>

<style lang="scss" scoped>

@keyframes spin
 {
     from{
         transform: rotate3d(0,1,0,0deg);
     }
     to{
         transform: rotate3d(0,1,0,360deg);
     }
    
}

.box{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.pic{
    height: 200px;
    width: 200px;
    animation: spin 3s infinite;
}

</style>