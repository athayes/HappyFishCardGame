<template>
  <div id="wrapper">
    <div id="app">
      <router-view :key="$route.fullPath"/>
    </div>
  </div>
</template>

<style>
#wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
}

#app {
  width: 667px;
  height: 375px;
}

.yellow-button {
  border-color: #fc3;
  background-color: #feb;
}

.green-button {
  background-color: #de8;
  border-color: #6c0;
  /*background-color: #cea;*/
  /*border-color: #390;*/
}

.purple-button {
  border-color: #eaf;
  background-color: #ddf;
}

.blue-button {
  background-color: #deefff;
  border-color: #6ab;
  /*background-color: #cff;*/
  /*border-color: #0071de;*/
}

.pink-button {
  background-color: #fdd;
  border-color: #f99;
}

.pinkish-button {
  background-color: #edc;
  border-color: #f99;
}

/* Look into using default for focus*/
/*input:focus, select:focus, textarea:focus {*/
/*  border: 2px solid #0071de;*/
/*}*/
</style>
