const AnyList = require('anylist');
const Item = require('anylist/lib/item');
const { exit } = require('process');
require('dotenv').config();
const al = new AnyList({email: process.env['ANYLIST_USERNAME'], password: process.env['ANYLIST_PASSWORD']});

al.login().then(async () => {
    const lists = await al.getLists();
    lists.forEach((el) => console.log(el.name))

    const shoppingList = await al.getListByName(process.env['ANYLIST_LIST_NAME']);
    let newItem = al.createItem({name: "Apples"});
    newItem = await shoppingList.addItem(newItem)

    exit();
}).finally(() => {
    al.teardown();
});