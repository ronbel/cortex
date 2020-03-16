<template>
    <div class="container">
        <div @click="$emit('back')" class="back"/>
            <h2>Snapshot 1111-eeeeeee-3124-51</h2>
            <div class="buttons-section">
                <div @click="selectedResult = 'pose'" :class="['button','result-option', {selected: selectedResult === 'pose'}]">Pose</div>
                <div @click="selectedResult = 'feelings'" :class="['button','result-option', {selected: selectedResult === 'feelings'}]">Feelings</div>
                <div @click="selectedResult = 'depth_image'" :class="['button','result-option', {selected: selectedResult === 'depth_image'}]">Depth</div>
                <div @click="selectedResult = 'color_image'" :class="['button','result-option', {selected: selectedResult === 'color_image'}]">Color</div>
            </div>
            <Feelings v-if="selectedResult === 'feelings'"/>
            <ImageView v-if="selectedResult === 'depth_image'"/>
            <ImageView v-if="selectedResult === 'color_image'"/>
            <Pose v-if="selectedResult === 'pose'"/>
    </div>
    
</template>

<script>

import Feelings from './Feelings'
import ImageView from './ImageView';
import Pose from './Pose'

export default {
    components:{
        Feelings,
        ImageView,
        Pose
    },
    data(){
        return {
            selectedResult: ''
        }
    }
    
}
</script>


<style lang="scss" scoped>
    .container{
        display: flex;
        flex: 1;
        flex-direction: column;
        align-items: center;
        padding-top: 15px;
        border-top: 3px gray solid;
        position: relative;
    }

    h2{
        color: #c3c3c3;
    }

    .buttons-section{
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 85%;
        margin-bottom: 20px;
    }

    .result-option{
        border: 1.5px silver solid;
        width: 135px;
        cursor: pointer;
        transition: border 200ms ease-in-out;

        &.selected{
            border-color: var(--main-color);
            border-width: 6px;
        }
    }

    .back{
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