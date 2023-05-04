<template>
  <div class="border">
    <h1>ㅋㅋㅋㅋㅋ</h1>
    <!-- <MyChild static-props="component에서 child로" 
    :my-props="dynamicProps"/> -->
    <MyChild static-props="component에서 child로" 
    :my-props="dynamicProps"
    @child-to-parent="parentGetEvent"
    @child-input="getDynamicData"
    />
    
  </div>
</template>

<script>
import MyChild from '@/components/MyChild'

export default {
  name: 'MyComponent',
  components: {
    MyChild,
  },
  data: function () {
    return {
      dynamicProps: "It's in data"
    }
  },
  methods: {
    parentGetEvent(inputData) {
      console.log("자식 컴포넌트에서 발생한 이벤트!")
      console.log(`child component로부터 ${inputData}를 받음!`)
    },
    getDynamicData(inputData) {
      console.log(`child component로부터 ${inputData}를 입력받음`)
    }
  }
}

</script>

<style>
  .border {
    border: solid;
  }
</style>