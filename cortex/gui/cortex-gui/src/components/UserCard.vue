<template>
    <div @click="onExapnd" :class="{card: true, expanded, 'selected': isSelected}">
        <div class="name-and-number">
            <span>{{user.username}}</span>
            <span>{{`Specimen #${user.user_id}`}}</span>
        </div>
        <p class="see-more-text" v-if="!expanded">Click to see more...</p>
      
        <Loading v-if="expanded && !fullUserData" :containerStyle="{'transform': 'scale(0.5) translateY(-180px)'}" />
            
        <div v-else-if="expanded && fullUserData" class="more-info">
            <div>
                <p>{{`Birthday: ${new Date(fullUserData.birthday * 1000).toLocaleDateString('en-GB')}`}}</p>
                <p>{{`Gender: ${gender}`}}</p>
            </div>
            <div @click.stop="$emit('snapshot-open', user.user_id)" class="see-snapshots">See Snapshots >></div>
        </div>
    </div>
</template>

<script>

import {getUser} from '../services/api.service';
import Loading from './Loading';

export default {
    data(){
        return {
            expanded: false,
            fullUserData: null
        }
    },
    methods:{
        onExapnd(){
            this.expanded = !this.expanded;
            if(!this.fullUserData){
              getUser(this.$props.user.user_id).then(data => setTimeout(() => this.fullUserData = data, 1000));
            }
        }
    },
    computed:{
        gender(){
            if(!this.fullUserData){
                return;
            }
            return ['Male','Female','Other'][this.fullUserData.gender];
        }
    },
    props: ['user', 'isSelected'],
    components: {Loading}
}
</script>

<style lang="scss" scoped>
    .card{
        background-color: #2f4353;
        background-image: linear-gradient(205deg, #2f4353 0%, #d2ccc4 74%);
        width: 90%;
        height: 100px;
        border-radius: 20px;
        transition: height 300ms ease-in-out, filter 300ms ease-in-out, transform 200ms ease-in-out;
        display: flex;
        flex-direction: column;
        cursor: pointer;

        &.expanded{
            height: 170px;
        }

        &.selected{
            transform: translateX(40px)
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