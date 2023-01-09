type Team = "red" | "blue" | "yellow"
type Health = 1 | 5 | 10

interface Player {   // ver2. type Player = {
    nickname: string,
    team: Team,
    health: Health
}

const nico :Player = {
    nickname: "nico",
    team: "yellow",
    health: 10
}