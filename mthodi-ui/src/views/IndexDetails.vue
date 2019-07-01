<template>
  <v-container fluid>
    <v-layout justify-space-between row fill-height>
      <v-layout column>
        <v-flex  xs12 md6>
          <IndexGraph/>
        </v-flex>
        <v-flex md6>
           <PeerList/>
        </v-flex>
      </v-layout>
      <v-flex md6>
        <IndexComponents/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
// @ is an alias to /src
import IndexComponents from "@/components/IndexComponents.vue";
import PeerList from "@/components/PeerList.vue";
import IndexGraph from "./IndexGraph.vue";

export default {
  name: "IndexDetails",
  props: ["symbol"],
  components: {
    IndexGraph,
    IndexComponents,
    PeerList
  }
};
</script>
