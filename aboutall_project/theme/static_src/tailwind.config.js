module.exports = {
    content: [
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
    ],
    theme: {
        fontFamily: {
            'body' : ['"Inter"', 'sans-serif'],
        },
        extend: {
            keyframes: {
                gradient: {
                  '0%': { backgroundPosition: '0% 50%' },
                  '50%': { backgroundPosition: '100% 50%' },
                  '100%': { backgroundPosition: '0% 50%' },
                },
            },
            animation: {
                gradient: 'gradient 5s ease infinite',
            },
            backgroundImage: {
                'gradient-rainbow': 'linear-gradient(270deg, #Sky-500, #FFFFFF)',
            },
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
