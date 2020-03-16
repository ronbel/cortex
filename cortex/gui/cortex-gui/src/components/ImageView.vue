<template>
    <div class='depth-container'>
        <div class="size">Size: 255x244</div>
        <a href="https://i.ytimg.com/vi/03HOhd4GI1w/maxresdefault.jpg" target="_blank">
        <img src="https://i.ytimg.com/vi/03HOhd4GI1w/maxresdefault.jpg" class="image" v-if="showImage"/>
        </a>
        <div @click="showImage=!showImage" class="show-button">{{`${showImage ? 'Hide' : 'Show'} Image`}}</div>
    </div>
</template>


<script>
export default {
    data(){
        return {
            showImage: false
        }
    }
}
</script>

<style lang="scss" scoped>

.size{
    color: var(--main-color);
    font-size: 25px;
    width: 100%;
    height: 40px;
}

.depth-container{
    display: flex;
    flex: 1;
    flex-direction: column;
    align-items: center;
}

.show-button{
    width: 150px;
    height: 50px;
    color: white;
    border: 2px white solid;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1.2rem;
    cursor: pointer;
    transition: border-color 200ms ease-in-out, color 200ms ease-in-out;

    &:hover{
        border-color: var(--main-color);
        color: var(--main-color);
    }

}

.image{
    width: 300px;
    height: 300px;
    margin-top: 10px;
    margin-bottom: 10px;
}

</style>