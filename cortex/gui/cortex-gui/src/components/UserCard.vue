<template>
    <div @click="expanded=!expanded" :class="{card: true, expanded}">
        <div class="name-and-number">
            <span>Dan Gittik</span>
            <span>Specimen #42</span>
        </div>
        <p class="see-more-text" v-if="!expanded">Click to see more...</p>

        <div class="more-info" v-if="expanded">
            <div>
                <p>Birthday: 4/3/1992</p>
                <p>Gender: Male</p>
            </div>
            <div @click.stop="$emit('snapshot-open', 1)" class="see-snapshots">See Snapshots >></div>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return {
            expanded: false
        }
    },
    props: ['user-info']
}
</script>

<style lang="scss" scoped>
    .card{
        background-color: #2f4353;
        background-image: linear-gradient(205deg, #2f4353 0%, #d2ccc4 74%);
        width: 90%;
        height: 100px;
        border-radius: 20px;
        transition: height 300ms ease-in-out, filter 300ms ease-in-out;
        display: flex;
        flex-direction: column;
        cursor: pointer;

        &.expanded{
            height: 170px;
        }

        .see-more-text{
            opacity: 0;
            transition: opacity 200ms ease-in-out;
        }

        &:hover{
            filter: brightness(1.3);

            .see-more-text{
                opacity: 1;
            }
        }
    }

    .name-and-number{
        display: flex;
        justify-content: space-between;
        align-items: center;
        width:90%;
        height: 50px;
        align-self: center;
        font-size: 1.3rem;
        margin-top: 15px;
    }

    .more-info{
        display: flex;
        flex: 1;
        padding-left: 15px;
        padding-right: 15px;
        align-items: center;
        justify-content: space-between;

        p{
            margin-top: 15px;
            margin-bottom: 0;
            text-align: left;
        }
    }

    .see-snapshots{
        font-size: 1.1rem;
        text-decoration-line: underline;
        color: var(--main-color);
        padding: 20px;

        &:hover{
            color: purple;
        }
    }

</style>