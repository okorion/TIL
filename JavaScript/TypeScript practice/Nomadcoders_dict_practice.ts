type Words = {
    [key:string]: string
}

class Dict {
    private words: Words
    constructor() {
        this.words = {}
    }
    add(word: Word) {
        if (this.words[word.term] === undefined) {
            this.words[word.term] = word.def;
        }
    }
    def(term:string){
        return this.words[term]
    }

    del(term:string){
        if (this.words[term] !== undefined) {
            console.log(`term이 ${this.words[term]}인 것 삭제 성공!`)
            this.words[term] = undefined;
        }
    }
}

class Word {
    constructor(
        public term: string,
        public def: string
    ) {}
}

const kimchi = new Word("kimchi", "한국의 음식");

const dict = new Dict()

dict.add(kimchi);
dict.def("kimchi")
dict.del("kimchi")