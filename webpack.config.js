const webpack = require('webpack');
var ManifestPlugin = require('webpack-manifest-plugin');
const path = require("path");

const ROOT_PATH = path.resolve(__dirname);
const BUILD_PATH = path.resolve(ROOT_PATH, 'backend/static/react');

const config = {
    devtool: 'eval-source-map',
    entry: {
        "homepage": __dirname + "/frontend/views/homepage.jsx",
        "about": __dirname + "/frontend/views/about.jsx",

        "navbar": __dirname + "/frontend/components/navbar.jsx",

        "clock": __dirname + "/frontend/widgets/clock.jsx",
        "marble_game": __dirname + "/frontend/games/marble_game.jsx"
    },
    output: {
        path: BUILD_PATH,
        publicPath: '/static/react/',
        filename: "[name].js"
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    },
    plugins: [
        new webpack.LoaderOptionsPlugin({
            minimize: true,
        }),
        new webpack.optimize.ModuleConcatenationPlugin(),

        new ManifestPlugin({
            stripSrc: true,
            fileName: './manifest.json',
        }),
    ],
    module: {
        rules: [{
            oneOf: [
                // Process JS with Babel.
                {
                    test: /\.(js|jsx|mjs)$/,
                    include: path.resolve(ROOT_PATH, 'frontend'),
                    loader: require.resolve("babel-loader"),
                    options: {
                        // This is a feature of `babel-loader` for webpack (not Babel itself).
                        // It enables caching results in ./node_modules/.cache/babel-loader/
                        // directory for faster rebuilds.
                        cacheDirectory: true
                    }
                },
                {
                    test: /\.css$/,
                    use: [ 'style-loader', 'css-loader' ]
                },
                {
                    test: /\.(png|jpe?g|gif)$/i,
                    use: [
                      {
                        loader: 'file-loader',
                        options: {
                            name: '[contenthash].[ext]',
                        }
                      },
                    ],
                },
            ]
        }]
    },
};
module.exports = config;