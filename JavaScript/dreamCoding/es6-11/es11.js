/**
 * Optional Chaining (ES11)
 * https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference
 */
{
    const person1 = {
        name: 'Ellie',
        job: {
            title: 'S/W Engineer',
            manager: {
                name: 'Bob',
            },
        },
    };
    const person2 = {
        name: 'Bob',
    };

    // BBBad!
    {
    function printManager(person) {
        console.log(person.job.manager.name);
    }
    printManager(person1);
    // printManager(person2);
    }

    // BBad!
    {
        function printManager(person) {
            console.log(
                person.job
                    ? person.job.manager
                        ? person.job.manager.name
                        : undefined
                    : undefined
            );
        }
        printManager(person1);
        printManager(person2);
    }

    // Bad
    {
        function printManager(person) {
            console.log(person.job && person.job.manager && person.job.manager.name);
        }
        printManager(person1);
        printManager(person2);
    }

    // Good!
    {
        function printManager(person) {
            console.log(person.job?.manager?.name);
        }
        printManager(person1);
        printManager(person2);
    }
}
console.clear()

/**
 * Nullish Coalescing Operator (ES11)
 * https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference
 */
{
    // Logical OR operator
    // false: false, '', 0, null, undefined
    {
        const name = 'Ellie';
        const userName = name || 'Guest';
        console.log(userName);
    }

    {
        const name = null;
        const userName = name || 'Guest';
        console.log(userName);
    }

    // Bad!
    {
        const name = '';
        const userName = name || 'Guest';
        console.log(userName);

        const num = 0;
        const message = num || 'undefined';
        console.log(message);
    }

    // Good!
    {
        const name = '';
        const userName = name ?? 'Guest';
        console.log(userName);

        const num = 0;
        const message = num ?? 'undefined';
        console.log(message);
    }
}