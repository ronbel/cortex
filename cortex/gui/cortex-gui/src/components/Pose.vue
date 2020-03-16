<template>
    <div class="pose-container">
        <div class="column">
            <h2>Translation</h2>
            <span>X:</span>
            <span>Y:</span>
            <span>Z:</span>
        </div>

        <div class="column">
            <h2>Rotation</h2>
            <span>X:</span>
            <span>Y:</span>
            <span>Z:</span>
            <span>W:</span>
        </div>
    </div>
</template>


<script>
export default {
    
}
</script>

<style lang="scss" scoped>
    .pose-container{
        display: flex;
        justify-content: space-between;
        padding: 20px;
        flex: 1;
        width: 80%;
    }

    .column{
        display: flex;
        flex-direction: column;

        h2{
            color: var(--main-color);
            font-size: 1.8rem;
        }

        span{
            color: white;
            font-size: 1.4rem;
            margin-bottom: 10px;
        }
    }
</style>