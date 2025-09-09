function benchmark(){
  const compute = (loopCount)=>{
    for (i=0;i<loopCount;i++){
      var salt = salt * Math.random() + Math.trunc(Math.random()*10)
    }
  };
    const now = Temporal.Now.instance();  
    compute(10);
    const diff = Temporal.Duration.from(now);
    console.log(diff.toString());
    console.log("YES")


  

}

benchmark();
console.log("A")
