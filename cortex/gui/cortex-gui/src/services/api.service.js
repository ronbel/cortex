import axios from 'axios';

const baseURL = '/api';

const api = axios.create({baseURL})

export async function getUsers(){
    return (await api.get('/users')).data;
}

export async function getUser(userId){
    return (await api.get(`/users/${userId}`)).data;
}

export async function getUserSnapshots(userId){
    return (await api.get(`/users/${userId}/snapshots`)).data;
}

export async function getSnapshot(userId, snapshotId){
    return (await api.get(`/users/${userId}/snapshots/${snapshotId}`)).data;
}

export async function getSnapshotResult(userId, snapshotId, resultName){
    return (await api.get(`/users/${userId}/snapshots/${snapshotId}/${resultName}`)).data;
}

export async function getSnapshotResultDataUrl(userId, snapshotId, resultName){
    return (await api.get(`/users/${userId}/snapshots/${snapshotId}/${resultName}/data`)).data;
}