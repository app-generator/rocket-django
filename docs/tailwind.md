## Tailwind

> Intro: What we offer, Webpack Integration

**Tailwind CSS** is a utility-first CSS framework packed with classes like `flex`, `pt-4`, `text-center` and `rotate-90` that can be composed to build any design, directly in your markup. **Rocket Django** interface is designed using Tailwind CSS and its components are from the `flowbite` plugin. **Flowbite** is an open-source library of over 600+ UI components, sections, and pages built with the utility classes from Tailwind CSS and designed in Figma. **Rocket Django** uses webpack integration to generate static assets that are used in the application. `Webpack` is a free and open-source module bundler for JavaScript. It is made primarily for JavaScript, but it can transform front-end assets such as HTML, CSS, and images if the corresponding loaders are included. Webpack takes modules with dependencies and generates static assets representing those modules.


### Understanding `tailwind.config.js`
`tailwind.config.js` is the configuration file for Tailwind CSS that allows you to add customization options.
```js
// tailwind.config.js
module.exports = {
  content: [
    './templates/**/*.html',
    './static/**/*.js',
    './node_modules/flowbite/**/*.js'
  ],
  ...
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        primary: { "50": "#eff6ff", "100": "#dbeafe", "200": "#bfdbfe", "300": "#93c5fd", "400": "#60a5fa", "500": "#3b82f6", "600": "#2563eb", "700": "#1d4ed8", "800": "#1e40af", "900": "#1e3a8a" }
      },
      ...
    },
  },

  plugins: [
    require('flowbite/plugin')
  ],
}

```
The `content` section is where you configure the paths to all of your HTML templates, JS components, and any other files that contain Tailwind class names. If you add new static files in directories other than the ones listed, you would need to add them to the `content` list.

The `plugins` section allows you to register plugins with Tailwind that can be used to generate extra utilities, components, base styles, or custom variants. FLowbite is registered as a plugin, therefore its vast library of components can be used in Rocket Django to increase development speed and create beautiful UIs.


### Understanding `webpack.config.js`
`webpack.config.js` is the configuration file for webpack that enables the generation of minimized static assets in the directory specified.
```js
module.exports = {
    entry: './static/assets/index.js',  // path to our input file
    output: {
        filename: '[name].bundle.js',  // output bundle file name
        path: path.resolve(__dirname, './static/dist'),  // path to our Django static directory
    },
    ...
};
```

The `entry` section signifies the entry point of the application, this should contain a link in the form of import statements to all your static assets that need to be bundled. It is assigned to `static/assets/index.js`.
```js
import './style.css';
import 'flowbite/dist/flowbite.js';
import './sidebar';
import './charts';
import './dark-mode';
```
If you add custom scripts and styling to Rocket Django, import them into `static/assets/index.js` to allow webpack to add them to the generated scripts.


### Getting started with Tailwind in Rocket Django
**Rocket Django** is styled using Tailwind CSS and components from Flowbite. To use these tools for further development, you need to have `Node.js` installed.

- If you have `Node.js` installed, run the following command in your terminal.
```bash
$ npm install
$ npm run dev
```
The command will install the packages needed for Tailwind and start up the development server for Tailwind.

- When the development server has been started, static files are generated in the `./static/dist` folder. This behaviour can be changed in the webpack configuration.

- Create a virtual environment to isolate your Python environment from your globally installed packages.
```sh
$ virtualenv env
$ source ./env/bin/activate             # Linux/Mac
$ source .\env\Scripts\activate         # Windows
(env) $
```

- After the virtual environment has been created, you can move on to install the dependencies for Rocket Django using the command below:
```sh
$ pip install -r requirements.txt
```

- Start the Django server and continue development to inspect changes as they are made using Tailwind's utility classes.
```sh
$ python manage.py runserver
```

Now the Django server is running, Tailwind's utility classes and Flowbite's components can be used in your templates to create beautiful interfaces.

### Adding a Flowbite component to a page
Flowbite contains over 600+ UI components, sections, and pages built with the utility classes from Tailwind CSS and designed in Figma.

- To use a component in Rocket Django, head to [Flowbite components](https://flowbite.com/docs/components/timeline/) page and select a component.

![Flowbite component page](https://github.com/app-generator/dummy/assets/57325382/f70f60d4-91d6-4863-9267-e1f8b7db689d)

- Copy the component and add the component to your Django template file. For this documentation, the component is added to `templates/dashboard/index.html`.

![Rocket Django flowbite component - Styled with Tailwind-Flowbite AppSeed](https://github.com/app-generator/dummy/assets/57325382/3712d2d2-621c-46b3-af4e-f0a2b150a15a)

We have successfully added a flowbite component to the homepage of the application. To access more Flowbite components, visit the `UI Component` link in the sidebar menu.

![Rocket Django UI component highlighted- Styled with Tailwind-Flowbite AppSeed](https://github.com/app-generator/dummy/assets/57325382/fd0e2509-c136-4e8a-951c-8b860086db8f)


## Conclusion
**Rocket Django** gives you the flexibility needed to build beautiful user interfaces, leveraging Tailwind CSS and Flowbite, increasing the development speed and improving the time it takes from development to deployment.

## ✅ Resources
- 👉 [Tailwind CSS](https://tailwindcss.com/docs/configuration) configuration
- 👉 [Webpack](https://webpack.js.org/configuration/) configuration
- 👉 [Flowbite](https://flowbite.com/docs/components/alerts/) components
- 👉 Join the [Community](https://discord.com/invite/fZC6hup) and chat with the team behind **Rocket Django**
