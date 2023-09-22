import AnyList from 'anylist';
import Item from 'anylist/lib/item.js';
import exit from 'process';
import 'dotenv/config'
const al = new AnyList({email: process.env['ANYLIST_USERNAME'], password: process.env['ANYLIST_PASSWORD']});

const sanitisedItems =

al.login().then(async () => {
    const lists = await al.getLists();
    lists.forEach((el) => console.log(el.name))

    const shoppingList = await al.getListByName(process.env['ANYLIST_LIST_NAME']);
    let newItem = al.createItem({name: "Apples"});
    //newItem = await shoppingList.addItem(newItem)

    sanitisedItems.forEach((item) => {
        console.log('Post item ' + item);
        newItem = al.createItem({ name: item });
        newItem = await shoppingList.addItem(newItem);
  
        /*if (newItem.name !== item) {
          throw new Error("Added item doesn't match what was returned - aborting");
        }*/
    process.exit();
}).finally(() => {
    al.teardown();
})});