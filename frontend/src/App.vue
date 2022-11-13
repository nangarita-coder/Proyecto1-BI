<template>
  <div>
    <el-form label-width="120px" class="demo-ruleForm">
      <el-form-item label="Review" prop="desc">
        <el-input v-model="review" type="textarea" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="enviar">Predict</el-button>
      </el-form-item>
    </el-form>
    <p>
      Stars predicted: {{ stars }}
    </p>
    <div style="display: flex; align-items: center;justify-content: center">
      <p v-for="star in stars" v-bind:key="star">
        ⭐
      </p>
    </div>

  </div>

</template>

<script>

export default {
  name: 'App',
  components: {
  },
  data() {
    return {
      review: "",
      stars: 0
    }
  },
  methods: {
    enviar: function (event) {
      const _this = this;
      var data = { 'text': _this.review }
      _this.stars = 0
      console.log(event)
      fetch(
        "http://localhost:8000/predict",
        {
          method: "POST",
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(data),
        },
      )
        .then(res => res.json())
        .then(json => {
          _this.stars = json.stars
          console.log(json)
        });
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: beige !important;
  margin-top: 60px;
}

.el-form-item__label {
  color: beige !important;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: medium !important;
}

html {
  background-color: black;
}
</style>
