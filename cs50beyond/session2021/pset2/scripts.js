/**
|-------------------------------------------------------------------------------
| scripts.js
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Mar 11, 2021
| Execution:    xdg-open quiz.html
|
| This program implements a simple quiz application.
|
*/

const questions = [
    {
        question: "What is Athena's favorite animal?",
        options: ["jellyfish", "penguins", "otters"],
        answer: "otters"
    },
    {
        question: "What is 10 + 10?",
        options: ["8", "20", "28", "30"],
        answer: "20"
    },
    {
        question: "What is the capital city of Finland?",
        options: ["Copenhagen", "Oslo", "Stockholm", "Helsinki"],
        answer: "Helsinki"
    },
    {
        question: "Which of the following elements is liquid at room temperature?",
        options: ["Mercury", "Lead", "Gold", "Silver"],
        answer: "Mercury"
    },
    {
        question: "What is the atomic number of carbon?",
        options: ["2", "10", "12", "200"],
        answer: "12"
    },
    {
        question: "Which of the following is a vegetable?",
        options: ["carrot", "banana", "orange", "kiwi"],
        answer: "carrot"
    }
];

let question_number = 0;
let correct = 0;

document.addEventListener("DOMContentLoaded", () => {
    load_question();
});

function load_question()
{
    document.querySelector("#question").innerHTML = questions[question_number].question;
    const options = document.querySelector("#options");
    options.innerHTML = "";
    
    for (const option of questions[question_number].options)
    {
        options.innerHTML += `<button class="option">${option}</button>`;
    }

    document.querySelectorAll(".option").forEach(option =>
    {
        option.onclick = () =>
        {
            if (option.textContent == questions[question_number].answer)
            {
                correct++;
            }

            question_number++;
            document.querySelector("#correct").innerHTML = `${correct} of ${question_number}`;

            if (question_number < questions.length)
            {
                load_question();
            }
            else
            {
                document.querySelector("#restart").innerHTML = "<button onclick=\"restart_quiz()\">Restart Quiz</button>"
            }
        }
    });
}

function restart_quiz()
{
    question_number = 0;
    correct = 0;
    document.querySelector("#correct").innerHTML = `${correct} of ${question_number}`;
    document.querySelector("#restart").innerHTML = "";
    load_question();
}

