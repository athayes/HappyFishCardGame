<template>
  <div id="wrapper">
    <div id="app">
      <router-view :key="$route.fullPath" />
    </div>
  </div>
</template>

