import AnyList from 'anylist';
import Item from 'anylist/lib/item.js';
import exit from 'process';
import 'dotenv/config'


export const handler = async (event) => {

  // event.body should contain something like ["apples","paper towel",""]
  if (!Array.isArray(event.items)) {
    return { statusCode: 400, body: 'body.items must be an array' }
  }
  
  const sanitisedItems = event.items.filter((i) => i.trim().length > 0);
  
  if(sanitisedItems.length === 0) {
    return { statusCode: 400, body: 'No items in array' }
  }

  const al = new AnyList({ email: process.env['ANYLIST_USERNAME'], password: process.env['ANYLIST_PASSWORD'] });

  await al.login()
  try {
    const lists = await al.getLists();
    lists.forEach((el) => console.log(el.name))

    const shoppingList = await al.getListByName(process.env['ANYLIST_LIST_NAME']);
    let newItem;
    for (const item of sanitisedItems) {
      console.log('Post item ' + item);
      newItem = al.createItem({ name: item });
      newItem = await shoppingList.addItem(newItem);

      if (newItem.name !== item) {
        throw new Error("Added item doesn't match what was returned - aborting");
      }
    };
    
  } finally {
    al.teardown();
  }
  return {
    statusCode: 200,
    body: event,
  };
};
