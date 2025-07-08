import React from "react";
import { Text } from "react-native";

const number2 = 4;
export const square = (inputNumber: number) => {
    return (Math.pow(inputNumber, 2));
}
export const TextCalculatedValue = () => {
    return(
        <Text>Calculation from module1: {square(number2)}</Text>
    );
}


export default number2;