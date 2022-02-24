<template>
  <div>
    <v-container>
      <v-card width="70vh" class="mx-auto">
        <v-card-title>Comparison Tool</v-card-title>
        <v-container>
          <v-row class="mx-2 mb-2">
            <v-select
              :items="items"
              label="Select a Model"
              outlined
              multiple
              v-model="selected"
            ></v-select>
          </v-row>
          <v-row class="mb-2 mr-2">
            <v-spacer></v-spacer>
            <v-btn
              color="primary"
              outlined
              rounded
              @click="printSelected(selected)"
              >COMPARE</v-btn
            >
          </v-row>
        </v-container>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import db from "../firebase";
import { collection, getDocs } from "firebase/firestore";

export default {
  name: "HomeView",
  data: () => ({
    items: [],
    selected: "",
    realScores: {},
    score: 0,
  }),
  methods: {
    printSelected() {
      for (let i = 0; i < this.selected.length; i++) {
        console.log(this.realScores[this.selected[i]]);
      }
    },
  },
  async created() {
    const querySnapshot = await getDocs(collection(db, "scores"));
    querySnapshot.forEach((doc) => {
      this.realScores = doc.data();
    });
    this.items = Object.keys(this.realScores);
  },
};
</script>
