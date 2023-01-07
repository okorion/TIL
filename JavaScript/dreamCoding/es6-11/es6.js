/**
 * Shorthand property names
 * https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Object_initializer
 *
 */

{
    const ellie1 = {
        name: 'Ellie',
        age: '18',
    };

    const name = 'Ellie';
    const age = '18';

    // Bad!
    const ellie2 = {
        name: name,
        age: age,
    };

    // Good!
    const ellie3 = {
        name,
        age,
    };

    console.log(ellie1, ellie2, ellie3);
}

/**
 * Destructuring Assignment
 * https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/
 *
 */
{
    // object
    const student = {
        name: 'Anna',
        level: 1,
    };

    // Bad!
    {
        const name = student.name;
        const level = student.level;
        console.log(name, level);
    }

    // Good!
    {
        const { name, level } = student;
        console.log(name, level);

        const { name: studentName, level: studentLevel } = student;
        console.log(studentName, studentLevel);
    }

    // array
    const animals = ['dog', 'cat'];

    // Bad!
    {
        const first = animals[0];
        const second = animals[1];
        console.log(first, second);
    }

    // Good!
    {
        const [first, second] = animals;
        console.log(first, second);
    }
}

/**
 * Spread Syntax
 * https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference
 *
 */
{
    const obj1 = { key: 'key1' };
    const obj2 = { key: 'key2' };
    const array = [obj1, obj2];

    // array copy
    const arrayCopy = [...array];
    console.log(array, arrayCopy);

    const arrayCopy2 = [...array, { key: 'key3' }];
    obj1.key = 'newKey';
    console.log(array, arrayCopy, arrayCopy2);

    // object copy
    const obj3 = { ...obj1 };
    console.log(obj3);

    // array concatenation
    const fruits1 = ['1', '2'];
    const fruits2 = ['3', '4'];
    const fruits = [...fruits1, ...fruits2];
    console.log(fruits);

    // object merge
    const dog1 = { dog: 'dog' };
    const dog2 = { dog: 'puppy' };
    const dog = { ...dog1, ...dog2 };
    console.log(dog);
}

/**
 * Default parameters
 * https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference
 */
{
    // Bad!
    {
        function printMessage(message) {
            if (message == null) {
                message = 'default message';
            }
            console.log(message);
        }

        printMessage('hello');
        printMessage();
    }

    // Good!
    {
        function printMessage(message = 'default message') {
            console.log(message);
        }

        printMessage('hello');
        printMessage();
    }
}

/**
 * Ternary Operator
 * https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference
 */
{
    const isCat = true;
    // Bad!
    {
        let component;
        if (isCat) {
            component = 'cat';
        } else {
            component = 'dog';
        }
        console.log(component);
    }

    // Good!
    {
        const component = isCat ? 'cat' : 'dog';
        console.log(component);
        console.log(isCat ? 'cat' : 'dog');
    }
    console.clear();
}

/**
 * Template Literals
 * https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference
 */
{
    const weather = 'cloudy';
    const temparature = '16℃';

    // Bad!
    console.log(
        'Today weather is ' + weather + ' and temparature is ' + temparature + '.'
    );
    // Good!
    console.log(`Today weather is ${weather} and temparature is ${temparature}.`);
}