<template>
  <v-app id="app">
    <NavBar />
    <v-content>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-content>
    <Footer />
  </v-app>
</template>

<script>

//import HelloWorld from './components/HelloWorld.vue'
import NavBar from "@/components/NavBar";
import Footer from "@/components/Footer"
export default {
  name: 'app',
  components: {
    NavBar,
    Footer
  }
}
</script>
