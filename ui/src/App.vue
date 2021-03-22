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
</style>
