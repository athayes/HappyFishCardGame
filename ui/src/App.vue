<template>
  <div id="wrapper">
    <div id="app">
      <router-view />
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

/* Look into using default for focus*/
/*input:focus, select:focus, textarea:focus {*/
/*  border: 2px solid #0071de;*/
/*}*/
</style>
