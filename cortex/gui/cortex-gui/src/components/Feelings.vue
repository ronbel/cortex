<template>
    <div @click="happiness=50" class="feelings-container">
        <ProgressBar font-size="20" text-fg-color="red" bar-color="red" class="progress-bar" text="Hunger" size="50" :val="happiness" max="100"/>
        <ProgressBar font-size="20" text-fg-color="blue" bar-color="blue" class="progress-bar" text="Thirst" size="50" val="14.2512" max="100"/>
        <ProgressBar font-size="20" text-fg-color="green" bar-color="green" class="progress-bar" text="Exhaustion" size="50" val="76.123" max="100"/>
        <ProgressBar font-size="20" text-fg-color="yellow" bar-color="yellow" class="progress-bar" text="Happiness" size="50" val="52.5" max="100"/>
    </div>
</template>

<script>

import ProgressBar from 'vue-simple-progress';

export default {
    data(){
        return {
            happiness: 0
        }
    },
    components:{
        ProgressBar
    }
    
}
</script>


<style lang="scss" scoped>
.feelings-container{
    display: flex;
    flex-direction: column;
    flex: 1;
    width: 100%;
    justify-content: center;
    align-items: 'center';
}

.progress-bar{
    margin-bottom: 10px;
    min-width: 350px;
}

</style>