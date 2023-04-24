const jsObject = {
	coffee: 'Americano',
	iceCream: 'Chocolate',
}

// Object -> JSON

const objToJSON = JSON.stringify(jsObject)

// JSON -> Object

const jsonToObject = JSON.parse(objToJSON)