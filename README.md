# Catalog

+1) Подключить СУБД PostgreSQL для работы в проекте.
- Создайте базу данных в ручном режиме.
- Внесите изменения в настройки подключения.

+2) В приложении каталога создайте модели:
- Product,
- Category.

+3) Для каждой модели опишите следующие поля:
- Product:
* наименование,
* описание,
* изображение (превью),
* категория,
* цена за штуку,
* дата создания,
* дата последнего изменения.
- Category:
* наименование,
* описание.

4) Перенесите отображение моделей в базу данных с помощью инструмента миграций. Для этого:
+ Создайте миграции для новых моделей.
+ Внесите изменения в модель категорий, добавьте поле created_at, примените обновление структуры с помощью миграций.
+ Откатите миграцию до состояния, когда поле created_at для модели категории еще не существовало, и удалите лишнюю миграцию.

5) + Для моделей категории и продукта настройте отображение в административной панели. 
     Для категорий выведите id и наименование в список отображения, а для продуктов выведите в список id, название, цену и категорию.

+ При этом интерфейс вывода продуктов настройте так, чтобы можно было результат отображения фильтровать по категории, 
 а также осуществлять поиск по названию и полю описания.

6) задание
+ Через инструмент shell заполните список категорий, а также выберите список категорий, применив произвольные рассмотренные фильтры. В качестве решения приложите скриншот.
+ Сформируйте фикстуры для заполнения базы данных.
+ Напишите кастомную команду, которая умеет заполнять данные в базу данных, при этом предварительно зачищать ее от старых данных.

7) * Дополнительное задание
- В контроллер отображения главной страницы добавьте выборку последних 5 товаров и вывод их в консоль.
- Создайте модель для хранения контактных данных и попробуйте вывести данные, заполненные через админку, на страницу с контактами.








