function biggiesize(arr){
    for (var i = 0; i < arr.length; i++){
        if(arr[i] > 0){
            arr[i] = 'big';
        }
    }
    return arr;
}


function printLowreturnHigh(arr){
    var min = arr[0];
    var max = arr[0];

    for (var i = 0; i < arr.length; i++){
        if(arr[i] < min){
            min = arr[i];
        }
        if(arr[i] > max){
            max = arr[i];
        }
    }
    console.log(min);
    return max;
}

function printOnereturnAnother(arr){
    console.log(arr.lenghth - 2);

    for (var i = 0; i < arr.length; i++){
        if(arr[i] % 2 === 1){
            break;
        }
    }
    return arr[i];
}


function doubleVision(arr){
    var arrnew = [];
    for (var i = 0; i < arr.length; i++){
        arr[i] = arr[i] * 2;
        arrnew.push(arr[i]);
    }
    return arrnew;
}


function countPositives(arr){
    var count = 0
    for (var i = 0; i < arr.length; i++){
        if(arr[i] > 0){
            count++;
        }
    }
    arr[arr.length - 1] = count;
    return arr;
}


function EvensandOdds(arr){
    var countodd = 0;
    var counteven = 0;

    for (var i = 0; i < arr.length; i++){
        if(arr[i] % 2 === 1){
            countodd +=1;
            counteven +=0;
        }
        else(arr[i] % 2 === 0){
            counteven +=1;
            countodd +=0;
        }
        if(countodd == 3){
            console.log("That's odd!")
        }
        if(counteven == 3){
            console.log("Even more so!")
        }
    }
}


function IncrementtheSeconds(arr){
    for (var i = 1; i < arr.length; i+=2){
        arr[i] = arr[i] + 1;
        console.log(arr[i]);
    }
    return arr;
}


function previouslengths(arr){
    for (var i = arr.length-1; i > 0; i--){
        arr[i] = arr[i -1].length;
    }
}


function AddseventoMost(arr){
    var arrnew = []
    for (var i = 1; i < arr.length; i++){
        arr[i] = arr[i] + 7;
        arrnew.push(arr[i]);
    }
    return arrnew;
}


function ReverseArray(arr){
    for(var i = 0; i < arr.length/2; i++){
        var temp = arr[i];
        arr[i] = arr[arr.length-1-i];
        arr[arr.length-1-i] = temp;
    }
}


function Outlook_Negative(arr){
    var arrnew = [];
    for (var i = 0; i < arr.length; i++){
        if(arr[i] > 0){
        arr[i] = arr[i] * -1
        }
    }
    return arrnew;
}


function alwaysHungry(arr){
    for (var i = 0; i < arr.length; i++){
        if(arr[i] == "food"){
            console.log("yummy");
        }
        else(arr[i] != "food"){
            console.log("I'm hungry");
        }
    }
    return arr;
}


function swap_t_Center(arr){
    for(var i = 0; i < arr.length/2; i++){
        var temp = arr[i];
        arr[i] = arr[arr.length-1-i];
        arr[arr.length-1-i] = temp;
    }
}


function scale_Array(arr, num){
    for(var i = 0; i < arr.length; i++){
        arr[i] = arr[i] * num;
    }
    return arr;
}