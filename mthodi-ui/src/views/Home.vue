<template>
  <v-container fluid>
    <v-layout row> 
      <!-- 9 colums for the indices table -->
      <v-flex md9>
        <IndexList/>
      </v-flex>
      <!-- 3 columns for the news headlines list -->
      <v-flex md3>
        <NewsHeadlines/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
// @ is an alias to /src
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
