<template>
  <v-container fluid>
    <v-layout row> 
      <v-flex md9>
        <IndexList/>
      </v-flex>
      <v-flex md3>
        <NewsHeadlines/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
// @ is an alias to /src
//import Map from "@/components/Map.vue";
import IndexList from "@/components/IndexList.vue";
import NewsHeadlines from "@/components/NewsHeadlines.vue";

export default {
  name: "Home",
  components: {
    IndexList,
    NewsHeadlines
  }
};
</script>
