// BLANK JS
// node blank.js
//----------------------------------------------------------------------------------------
// //max string length 
// function maxString(pali){
//     let paliArray = pali.split("")
//     // return paliArray;
//     for (let i=0;i<pali.length;i++){
//         for (let i=0;i<pali.length;i++){
//             if (paliArray[i] === paliArray.pop()){
//                 return "PALANDROME"
//             } else {
//                 return "NOPE!"
//             }
//         };
//     };
// };

// console.log(
//     maxString("HANNAHHANNAH"),
//     maxString("BOBOBOB"),
//     maxString("CAT"),
//     maxString("MOOOM"),
// )
//----------------------------------------------------------------------------------------

// // HASH MAP WITH HIGHEST INDEX NUMBER
// function maxStringLength(x){
//     let myMap = new Object;
//     for (let i=0;i<x.length;i++){
//         for (let j=0;j<x.length;j++){
//             myMap[x[i]] = i;
//         };
//     };
//     return myMap;
// };

// console.log(
//     maxStringLength(["A", "B", "C", "A", "B", "B", "D"]) //{a:3, b:5, c:2}
// )
//----------------------------------------------------------------------------------------

// //Check if valid parenthesis
// // return xarr[0]; // {
// // return chart[xarr[0]]; // }
// function paraChecker(x){
//     //splits up initial bracket string into array
//     let xarr = x.split("");
//     //Chart to compate open/close brackets
//     let chart = {'{':'}','[':']','(':')' };
//     //FOR LOOP
//     for (let i=0; i<xarr.length; i++){
//         //CHECK IF 1st AND LAST MATCH
//         //POP to remove last array element
//         if (chart[xarr[i]] === xarr.pop() && xarr.length % 2 === 0){
//             //REPLACE CURRENT ARRAY WITH ORIGINAL MINUS 1st
//             xarr = xarr.splice(i+1,xarr.length);
//         } else {
//             return false;
//         }
//         return true;
//     }
// };
// console.log(
//     paraChecker('{[()]}')
// )
//----------------------------------------------------------------------------------------
//

/*-----------------------------------------------------------------
  Challenge: 30-totalTaskTime
  
  Difficulty:  Difficult
  
  Prompt:
  
  - Write a function called totalTaskTime that accepts two arguments.
  - The first argument is an array of integers referred to as a "queue".  Each integer in the queue represents a "task", more specifically, the amount of time to complete that task.
  - The second argument is an integer representing the number of CPU "threads" available to process all of the tasks in the queue.
  - The totalTaskTime function should return an integer representing the total time it is going to take to complete all of the tasks in the queue.
  - You may mutate the "queue" array (first argument) if you wish.
  
  Hint:
  
  - Solve it with paper and pencil first.  Look for patterns and generalize.  Pseudocode!
  
  Examples:
  
  totalTaskTime( [], 1 ) // => 0
  totalTaskTime( [4, 2, 5], 1 ) // => 11
  totalTaskTime( [5, 8], 2 ) // => 8
  totalTaskTime( [4, 2, 10], 2 ) // => 12
  totalTaskTime( [2, 2, 3, 3, 4, 4], 2 ) //=> 9
  totalTaskTime( [5, 2, 6, 8, 7, 2], 3 ) // => 12
  -----------------------------------------------------------------*/
  // Your solution for 30- here:
  
// function totalTaskTime(queue,threads){
//     let time = 0;

//     for (let j=0; queue.length > 0; j++){ //------------------------------
//         if (queue.length>1){
//             //RUNNING FULL NUMBER OF THREADS
//             for (let i = 0; i < threads; i++){
//                 queue.splice(i,1,queue[i]-1); //0
//                 queue = queue.filter(task => task > 0) //REMOVE 0's
//             }
//             // console.log("X: "+queue);
//         }
//         //ONLY RUN SINGLE THREAD
//         if (queue.length === 1 && queue.length !== 0){
//             queue = [queue[0]-1]
//             queue = queue.filter(task => task > 0) //REMOVE 0's
//             // console.log("Y: "+queue);
//         }
//         //IF NO TASKS TO COMPLETE...
//         if (queue.length <= 0){
//             // console.log("Z:")
//         }
//         time = time+1;
//     } //--------------------------------------------------------------------

//     return "TIME:"+time;+"secs"
// };

// console.log(
//     totalTaskTime( [], 1 ), // => 0
//     totalTaskTime( [4, 2, 5], 1 ), // => 11
//     totalTaskTime( [5, 8], 2 ), // => 8
//     totalTaskTime( [4, 2, 10], 2 ), // => 12
//     totalTaskTime( [2, 2, 3, 3, 4, 4], 2 ), //=> 9
//     totalTaskTime( [5, 2, 6, 8, 7, 2], 3 ) // => 12    )
// )

    // currentTasks = currentTasks.map(task=>task-1)
    // currentTasks = currentTasks.filter(task => task > 0)
    // console.log(currentTasks)

    // queue = [...queue, 1]
    // let temp = queue[0]-1;
    // queue.splice(0,1);
    // queue = [temp,...queue]

    // queue.splice(0,1,queue[0]-1); //0
    // queue = queue.filter(task => task > 0) //REMOVE 0's

    // return queue;
//--------------------------------------------------------------------------------------







