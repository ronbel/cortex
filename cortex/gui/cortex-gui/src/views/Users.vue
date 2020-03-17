<template>
  <div class="container">
    <router-link exact to="/" class="button back-button">Back</router-link>

    <div class="users-section">
      <h1 class="users-title">User List</h1>
      <Loading v-if="!usersReady" />
      <div v-else class="user-list">
        <UserCard
          v-for="user in usersList"
          :key="user.user_id"
          :user="user"
          @snapshot-open="selectUser"
          :isSelected="selectedUser === user.user_id"
        />
      </div>
    </div>

    <transition name="slide">
      <SnapshotSection :userId="selectedUser" v-if="selectedUser !== null" @close="selectUser(null)" />
    </transition>
  </div>
</template>


<script>
import Loading from "../components/Loading";
import UserCard from "../components/UserCard";
import SnapshotSection from "../components/SnapshotSection";
import { getUsers } from "../services/api.service";

export default {
  data() {
    return {
      selectedUser: null,
      usersReady: false,
      usersList: []
    };
  },
  components: {
    Loading,
    UserCard,
    SnapshotSection
  },
  methods: {
    selectUser(id) {
      this.selectedUser = this.selectedUser === id ? null : id;
    }
  },
  created() {
    getUsers()
      .then(data => {
        setTimeout(() => {
          this.usersList = data;
          this.usersReady = true;
        }, 1500);
      });
  }
};
</script>


<style lang="scss" scoped>
.container {
  display: flex;
  flex: 1;
  padding-top: 50px;
  padding-left: 150px;
  padding-right: 30px;
  justify-content: space-between;
}

.back-button {
  position: absolute;
  top: 30px;
  left: 30px;
}

.users-section {
  height: 90vh;
  width: 30vw;
  background-color: var(--secondary-color);
  border-radius: 10%;
  display: flex;
  flex-direction: column;
  padding-left: 25px;
  padding-bottom: 30px;
  padding-right: 25px;
}

.users-title {
  color: var(--main-color);
}

.user-list {
  display: grid;
  grid-template-columns: 1fr;
  grid-row-gap: 15px;
  overflow-y: scroll;
  flex: 1;

  &::-webkit-scrollbar-track {
    -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.1);
    background-color: #f5f5f5;
    border-radius: 10px;
  }

  &::-webkit-scrollbar {
    width: 10px;
    background-color: #f5f5f5;
    border-radius: 10px;
  }

  &::-webkit-scrollbar-thumb {
    border-radius: 10px;
    background-color: var(--main-color);
  }
}

.slide-leave-active,
.slide-enter-active {
  transition: transform 0.5s ease;
}

.slide-enter,
.slide-leave-to {
  transform: translateX(150%);
}

.slide-enter-to,
.slide-leave {
  transform: translateX(0);
}
</style>