<template>
  <div class="border">
    <h1>ㅋㅋㅋㅋㅋ</h1>
    <MyChild/>
  </div>
</template>

<script>
import MyChild from '@/components/MyChild'

export default {
  name: 'MyComponent',
  components: {
    MyChild,
  }
}

</script>

<style>
  .border {
    border: solid;
  }
</style>